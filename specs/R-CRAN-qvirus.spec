%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qvirus
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quantum Computing for Analyzing CD4 Lymphocytes and Antiretroviral Therapy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 

%description
Resources, tutorials, and code snippets dedicated to exploring the
intersection of quantum computing and artificial intelligence (AI) in the
context of analyzing Cluster of Differentiation 4 (CD4) lymphocytes and
optimizing antiretroviral therapy (ART) for human immunodeficiency virus
(HIV). With the emergence of quantum artificial intelligence and the
development of small-scale quantum computers, there's an unprecedented
opportunity to revolutionize the understanding of HIV dynamics and
treatment strategies. This project leverages the R package 'qsimulatR'
(Ostmeyer and Urbach, 2023,
<https://CRAN.R-project.org/package=qsimulatR>), a quantum computer
simulator, to explore these applications in quantum computing techniques,
addressing the challenges in studying CD4 lymphocytes and enhancing ART
efficacy.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
