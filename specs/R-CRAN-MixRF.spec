%global __brp_check_rpaths %{nil}
%global packname  MixRF
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Random-Forest-Based Approach for Imputing Clustered IncompleteData

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-foreach 

%description
It offers random-forest-based functions to impute clustered incomplete
data. The package is tailored for but not limited to imputing multitissue
expression data, in which a gene's expression is measured on the collected
tissues of an individual but missing on the uncollected tissues.

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
