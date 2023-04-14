%global __brp_check_rpaths %{nil}
%global packname  pedigreemm
%global packver   0.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Pedigree-based mixed-effects models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-Matrix >= 1.0
BuildRequires:    R-methods 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-Matrix >= 1.0
Requires:         R-methods 

%description
Fit pedigree-based mixed-effects models.

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
