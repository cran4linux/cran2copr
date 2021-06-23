%global __brp_check_rpaths %{nil}
%global packname  OHPL
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Ordered Homogeneity Pursuit Lasso for Group Variable Selection

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-mvtnorm 

%description
Ordered homogeneity pursuit lasso (OHPL) algorithm for group variable
selection proposed in Lin et al. (2017)
<DOI:10.1016/j.chemolab.2017.07.004>. The OHPL method exploits the
homogeneity structure in high-dimensional data and enjoys the grouping
effect to select groups of important variables automatically. This feature
makes it particularly useful for high-dimensional datasets with strongly
correlated variables, such as spectroscopic data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
