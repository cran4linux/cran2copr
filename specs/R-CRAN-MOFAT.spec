%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MOFAT
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum One-Factor-at-a-Time Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SLHD 
BuildRequires:    R-stats 
Requires:         R-CRAN-SLHD 
Requires:         R-stats 

%description
Identifying important factors from a large number of potentially important
factors of a highly nonlinear and computationally expensive black box
model is a difficult problem. Xiao, Joseph, and Ray (2022)
<doi:10.1080/00401706.2022.2141897> proposed Maximum One-Factor-at-a-Time
(MOFAT) designs for doing this. A MOFAT design can be viewed as an
improvement to the random one-factor-at-a-time (OFAT) design proposed by
Morris (1991) <doi:10.1080/00401706.1991.10484804>. The improvement is
achieved by exploiting the connection between Morris screening designs and
Monte Carlo-based Sobol' designs, and optimizing the design using a
space-filling criterion. This work is supported by a U.S. National Science
Foundation (NSF) grant CMMI-1921646
<https://www.nsf.gov/awardsearch/showAward?AWD_ID=1921646>.

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
