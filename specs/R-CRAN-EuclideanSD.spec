%global __brp_check_rpaths %{nil}
%global packname  EuclideanSD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Euclidean View of Center and Spread

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-shiny 

%description
Illustrates the concepts developed in Sarkar and Rashid (2019,
ISSN:0025-5742)
<http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiH4deL3q3xAhWX73MBHR_wDaYQFnoECAUQAw&url=https%%3A%%2F%%2Fwww.indianmathsociety.org.in%%2Fmathstudent-part-2-2019.pdf&usg=AOvVaw3SY--3T6UAWUnH5-Nj6bSc>.
This package helps a user guess four things (mean, MD, scaled MSD, and
RMSD) before they get the SD. 1) The package displays the Empirical
Cumulative Distribution Function (ECDF) of the given data. The user must
choose the value of the mean by equating the areas of two colored (blue
and green) regions. The package gives feedback to improve the choice until
it is correct. Alternatively, the reader may continue with a different
guess for the center (not necessarily the mean). 2) The user chooses the
values of the Mean Deviation (MD) based on the ECDF of the deviations by
equating the areas of two newly colored (blue and green) regions, with
feedback from the package until the user guesses correctly. 3) The user
chooses the Scaled Mean Squared Deviation (MSD) based on the ECDF of the
scaled square deviations by equating the areas of two newly colored (blue
and green) regions, with feedback from the package until the user guesses
correctly. 4) The user chooses the Root Mean Squared Deviation (RMSD) by
ensuring that its intersection with the ECDF of the deviations is at the
same height as the intersection between the scaled MSD and the ECDF of the
scaled squared deviations. Additionally, the intersection of two blue
lines (the green dot) should fall on the vertical line at the maximum
deviation. 5) Finally, if the mean is chosen correctly, only then the user
can view the population SD (the same as the RMSD) and the sample SD
(sqrt(n/(n-1))*RMSD) by clicking the respective buttons. If the mean is
chosen incorrectly, the user is asked to correct it.

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
