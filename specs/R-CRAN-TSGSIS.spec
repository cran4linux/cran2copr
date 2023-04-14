%global __brp_check_rpaths %{nil}
%global packname  TSGSIS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Two Stage-Grouped Sure Independence Screening

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 
Requires:         R-stats 

%description
To provide a high dimensional grouped variable selection approach for
detection of whole-genome SNP effects and SNP-SNP interactions, as
described in Fang et al. (2017, under review).

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
