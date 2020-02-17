%global packname  rTorch
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          R Bindings to 'PyTorch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-logging 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-logging 
Requires:         R-CRAN-reticulate 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 

%description
'R' implementation and interface of the Machine Learning platform
'PyTorch' <https://pytorch.org/> developed in 'Python'. It requires a
'conda' environment with 'torch' and 'torchvision' to provide 'PyTorch'
functions, methods and classes. The key object in 'PyTorch' is the tensor
which is in essence a multidimensional array. These tensors are fairly
flexible to perform calculations in CPUs as well as 'GPUs' to accelerate
the process.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/old_R
%doc %{rlibdir}/%{packname}/old_tests
%doc %{rlibdir}/%{packname}/old_vignettes
%doc %{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
