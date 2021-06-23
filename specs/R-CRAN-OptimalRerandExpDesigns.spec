%global __brp_check_rpaths %{nil}
%global packname  OptimalRerandExpDesigns
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Rerandomization Experimental Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-GreedyExperimentalDesign >= 1.3
BuildRequires:    R-CRAN-momentchi2 >= 0.1.5
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-GreedyExperimentalDesign >= 1.3
Requires:         R-CRAN-momentchi2 >= 0.1.5
Requires:         R-stats 

%description
This is a tool to find the optimal rerandomization threshold in
non-sequential experiments. We offer three procedures based on assumptions
made on the residuals distribution: (1) normality assumed (2) excess
kurtosis assumed (3) entire distribution assumed. Illustrations are
included. Also included is a routine to unbiasedly estimate Frobenius
norms of variance-covariance matrices. Details of the method can be found
in "Optimal Rerandomization via a Criterion that Provides Insurance
Against Failed Experiments" Adam Kapelner, Abba M. Krieger, Michael Sklar
and David Azriel (2020) <arXiv:1905.03337>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
