%global packname  ruta
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Implementation of Unsupervised Neural Architectures

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.2.3
BuildRequires:    R-stats >= 3.2.3
BuildRequires:    R-CRAN-R.utils >= 2.7.0
BuildRequires:    R-CRAN-keras >= 2.2.4
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-utils 
Requires:         R-graphics >= 3.2.3
Requires:         R-stats >= 3.2.3
Requires:         R-CRAN-R.utils >= 2.7.0
Requires:         R-CRAN-keras >= 2.2.4
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-utils 

%description
Implementation of several unsupervised neural networks, from building
their architecture to their training and evaluation. Available networks
are auto-encoders including their main variants: sparse, contractive,
denoising, robust and variational, as described in Charte et al. (2018)
<doi:10.1016/j.inffus.2017.12.007>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
