%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bcc
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Beta Control Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Applies Beta Control Charts to defined values. The Beta Chart presents
control limits based on the Beta probability distribution, making it
suitable for monitoring fraction data from a Binomial distribution as a
replacement for p-Charts. The Beta Chart has been applied in three real
studies and compared with control limits from three different schemes. The
comparative analysis showed that: (i) the Beta approximation to the
Binomial distribution is more appropriate for values confined within the
[0, 1] interval; and (ii) the proposed charts are more sensitive to the
average run length (ARL) in both in-control and out-of-control process
monitoring. Overall, the Beta Charts outperform the Shewhart control
charts in monitoring fraction data. For more details, see Ângelo Márcio
Oliveira Sant’Anna and Carla Schwengber ten Caten (2012)
<doi:10.1016/j.eswa.2012.02.146>.

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
