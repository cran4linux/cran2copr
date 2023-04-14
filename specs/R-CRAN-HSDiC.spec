%global __brp_check_rpaths %{nil}
%global packname  HSDiC
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Homogeneity and Sparsity Detection Incorporating PriorConstraint Information

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-quadprog 
Requires:         R-Matrix 

%description
We explore sparsity and homogeneity of regression coefficients
incorporating prior constraint information. A general pairwise fusion
approach is proposed to deal with the sparsity and homogeneity detection
when combining prior convex constraints. We develop an modified
alternating direction method of multipliers algorithm (ADMM) to obtain the
estimators.

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
