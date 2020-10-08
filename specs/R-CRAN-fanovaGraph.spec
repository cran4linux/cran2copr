%global packname  fanovaGraph
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Building Kriging Models from FANOVA Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiceKriging >= 1.4
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-DiceKriging >= 1.4
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-igraph 

%description
Estimation and plotting of a function's FANOVA graph to identify the
interaction structure and fitting, prediction and simulation of a Kriging
model modified by the identified structure. The interactive function
plotManipulate() can only be run on the 'RStudio IDE' with 'RStudio'
package 'manipulate' loaded. 'RStudio' is freely available
(<https://rstudio.com/>), and includes package 'manipulate'. The
equivalent function plotTk() bases on CRAN Repository packages only. For
further information on the method see Fruth, J., Roustant, O., Kuhnt, S.
(2014) <doi:10.1016/j.jspi.2013.11.007>.

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
