%global __brp_check_rpaths %{nil}
%global packname  fpa
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Fixation Pattern Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-fields 

%description
Spatio-temporal Fixation Pattern Analysis (FPA) is a new method of
analyzing eye movement data, developed by Mr. Jinlu Cao under the
supervision of Prof. Chen Hsuan-Chih at The Chinese University of Hong
Kong, and Prof. Wang Suiping at the South China Normal Univeristy. The
package "fpa" is a R implementation which makes FPA analysis much easier.
There are four major functions in the package: ft2fp(), get_pattern(),
plot_pattern(), and lineplot(). The function ft2fp() is the core function,
which can complete all the preprocessing within moments. The other three
functions are supportive functions which visualize the eye fixation
patterns.

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
