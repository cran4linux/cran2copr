%global __brp_check_rpaths %{nil}
%global packname  fmriqa
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Functional MRI Quality Assurance Routines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-optparse 
Requires:         R-tcltk 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-pracma 

%description
Methods for performing fMRI quality assurance (QA) measurements of test
objects. Heavily based on the fBIRN procedures detailed by Friedman and
Glover (2006) <doi:10.1002/jmri.20583>.

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
