%global packname  NVCSSL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Nonparametric Varying Coefficient Spike-and-Slab Lasso

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-Matrix 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-grpreg 
Requires:         R-Matrix 

%description
EM algorithm for fitting Bayesian varying coefficient models with the
nonparametric varying coefficient spike-and-slab lasso of Bai et al.
(2020) <arXiv:1907.06477>. Also fits penalized frequentist varying
coefficient models with the group lasso, group smoothly clipped absolute
deviation, and group minimax concave penalty.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
