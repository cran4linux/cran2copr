%global packname  hglasso
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Learning graphical models with hubs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-fields 

%description
Implements the hub graphical lasso and hub covariance graph proposal by
Tan, KM., London, P., Mohan, K., Lee, S-I., Fazel, M., and Witten, D.
(2014). Learning graphical models with hubs. To appear in Journal of
Machine Learning Research. arXiv.org/pdf/1402.7349.pdf.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
