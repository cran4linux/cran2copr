%global packname  segmented
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Regression Models with Break-Points / Change-Points Estimation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Given a regression model, segmented `updates' it by adding one or more
segmented (i.e., piece-wise linear) relationships. Several variables with
multiple breakpoints are allowed. The estimation method is discussed in
Muggeo (2003, <doi:10.1002/sim.1545>) and illustrated in Muggeo (2008,
<https://www.r-project.org/doc/Rnews/Rnews_2008-1.pdf>). An approach for
hypothesis testing is presented in Muggeo (2016,
<doi:10.1080/00949655.2016.1149855>), and interval estimation for the
breakpoint is discussed in Muggeo (2017, <doi:10.1111/anzs.12200>).

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

%files
%{rlibdir}/%{packname}
