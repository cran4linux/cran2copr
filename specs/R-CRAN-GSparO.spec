%global packname  GSparO
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Group Sparse Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ThreeWay 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-ThreeWay 
Requires:         R-CRAN-ggplot2 

%description
Approaches a group sparse solution of an underdetermined linear system. It
implements the proximal gradient algorithm to solve a lower regularization
model of group sparse learning. For details, please refer to the paper "Y.
Hu, C. Li, K. Meng, J. Qin and X. Yang. Group sparse optimization via
l_{p,q} regularization. Journal of Machine Learning Research, to appear,
2017".

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
