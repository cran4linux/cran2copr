%global __brp_check_rpaths %{nil}
%global packname  fluoSurv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate Insect Survival from Fluorescence Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
Use spectrophotometry measurements performed on insects as a way to infer
pathogens virulence. Insect movements cause fluctuations in fluorescence
signal, and functions are provided to estimate when the insect has died as
the moment when variance in autofluorescence signal drops to zero. The
package provides functions to obtain this estimate together with functions
to import spectrophotometry data from a Biotek microplate reader. Details
of the method are given in Parthuisot et al. (2018) <doi:10.1101/297929>.

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
