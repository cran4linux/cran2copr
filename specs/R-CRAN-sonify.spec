%global __brp_check_rpaths %{nil}
%global packname  sonify
%global packver   0.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Data Sonification - Turning Data into Sound

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tuneR >= 1.3.1
Requires:         R-CRAN-tuneR >= 1.3.1

%description
Sonification (or audification) is the process of representing data by
sounds in the audible range. This package provides the R function sonify()
that transforms univariate data, sampled at regular or irregular
intervals, into a continuous sound with time-varying frequency. The ups
and downs in frequency represent the ups and downs in the data. Sonify
provides a substitute for R's plot function to simplify data analysis for
the visually impaired.

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
