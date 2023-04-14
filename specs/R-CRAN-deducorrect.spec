%global __brp_check_rpaths %{nil}
%global packname  deducorrect
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          3%{?dist}%{?buildtag}
Summary:          Deductive Correction, Deductive Imputation, and DeterministicCorrection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-editrules >= 2.9.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-editrules >= 2.9.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
A collection of methods for automated data cleaning where all actions are
logged.

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
