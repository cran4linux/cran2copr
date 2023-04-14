%global __brp_check_rpaths %{nil}
%global packname  SequentialDesign
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Observational Database Study Planning using Exact SequentialAnalysis for Poisson and Binomial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Sequential 
BuildRequires:    R-stats 
Requires:         R-CRAN-Sequential 
Requires:         R-stats 

%description
Functions to be used in conjunction with the 'Sequential' package that
allows for planning of observational database studies that will be
analyzed with exact sequential analysis. This package supports Poisson-
and binomial-based data. The primary function, seq_wrapper(...), accepts
parameters for simulation of a simple exposure pattern and for the
'Sequential' package setup and analysis functions. The exposure matrix is
used to simulate the true and false positive and negative populations
(Green (1983) <doi:10.1093/oxfordjournals.aje.a113521>, Brenner (1993)
<doi:10.1093/oxfordjournals.aje.a116805>). Functions are then run from the
'Sequential' package on these populations, which allows for the
exploration of outcome misclassification in data.

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
