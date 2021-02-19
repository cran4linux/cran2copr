%global packname  CDFt
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Downscaling and Bias Correction via Non-Parametric CDF-Transform

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Statistical downscaling and bias correction (model output statistics)
method based on cumulative distribution functions (CDF) transformation.
See Michelangeli, Vrac, Loukos (2009) Probabilistic downscaling
approaches: Application to wind cumulative distribution functions.
Geophysical Research Letters, 36, L11708, <doi:10.1029/2009GL038401>. ;
and Vrac, Drobinski, Merlo, Herrmann, Lavaysse, Li, Somot (2012) Dynamical
and statistical downscaling of the French Mediterranean climate:
uncertainty assessment. Nat. Hazards Earth Syst. Sci., 12, 2769-2784,
www.nat-hazards-earth-syst-sci.net/12/2769/2012/,
<doi:10.5194/nhess-12-2769-2012>.

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
