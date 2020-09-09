%global packname  rainfarmr
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Precipitation Downscaling with the RainFARM Method

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
An implementation of the RainFARM (Rainfall Filtered Autoregressive Model)
stochastic precipitation downscaling method (Rebora et al. (2006)
<doi:10.1175/JHM517.1>). Adapted for climate downscaling according to
D'Onofrio et al. (2018) <doi:10.1175/JHM-D-13-096.1> and for complex
topography as in Terzago et al. (2018) <doi:10.5194/nhess-18-2825-2018>.
The RainFARM method is based on the extrapolation to small scales of the
Fourier spectrum of a large-scale precipitation field, using a fixed
logarithmic slope and random phases at small scales, followed by a
nonlinear transformation of the resulting linearly correlated stochastic
field. RainFARM allows to generate ensembles of spatially downscaled
precipitation fields which conserve precipitation at large scales and
whose statistical properties are consistent with the small-scale
statistics of observed precipitation, based only on knowledge of the
large-scale precipitation field.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
