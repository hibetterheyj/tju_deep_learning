def load_data(train_path='train/', test_path='test/'):
    train_list = glob(osp.join(train_path, '*.png'))
    pattern = re.compile(r'num(\d).png')
    train_id = np.array([float(pattern.search(img_name).groups()[0]) for img_name in train_list])
    train_data = np.concatenate([np.array(Image.open(img_name)).reshape((1, 784))for img_name in tqdm_notebook(train_list, leave=False)],
                                axis=0).astype(np.float)

    test_list = glob(osp.join(test_path, '*.png'))
    test_id = np.array([float(pattern.search(img_name).groups()[0]) for img_name in test_list])
    test_data = np.concatenate([np.array(Image.open(img_name)).reshape((1, 784)) for img_name in tqdm_notebook(test_list, leave=False)],
                               axis=0).astype(np.float)

    return train_data, train_id, test_data, test_id