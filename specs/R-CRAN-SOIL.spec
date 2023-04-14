%global __brp_check_rpaths %{nil}
%global packname  SOIL
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Sparsity Oriented Importance Learning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-brglm2 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-brglm2 

%description
Sparsity Oriented Importance Learning (SOIL) provides a new variable
importance measure for high dimensional linear regression and logistic
regression from a sparse penalization perspective, by taking into account
the variable selection uncertainty via the use of a sensible model
weighting. The package is an implementation of Ye, C., Yang, Y., and Yang,
Y. (2017+).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
