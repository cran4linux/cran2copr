%global __brp_check_rpaths %{nil}
%global packname  nparACT
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Parametric Measures of Actigraphy Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-zoo 
Requires:         R-tools 

%description
Computes interdaily stability (IS), intradaily variability (IV) & the
relative amplitude (RA) from actigraphy data as described in Blume et al.
(2016) <doi: 10.1016/j.mex.2016.05.006> and van Someren et al. (1999)
<doi: 10.3109/07420529908998724>. Additionally, it also computes L5 (i.e.
the 5 hours with lowest average actigraphy amplitude) and M10 (the 10
hours with highest average amplitude) as well as the respective start
times. The flex versions will also compute the L-value for a user-defined
number of minutes. IS describes the strength of coupling of a rhythm to
supposedly stable zeitgebers. It varies between 0 (Gaussian Noise) and 1
for perfect IS. IV describes the fragmentation of a rhythm, i.e. the
frequency and extent of transitions between rest and activity. It is near
0 for a perfect sine wave, about 2 for Gaussian noise and may be even
higher when a definite ultradian period of about 2 hrs is present. RA is
the relative amplitude of a rhythm. Note that to obtain reliable results,
actigraphy data should cover a reasonable number of days.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
