%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  perARMA
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Periodic Time Series Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-gnm 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-gnm 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-signal 
Requires:         R-stats 

%description
Identification, model fitting and estimation for time series with periodic
structure. Additionally, procedures for simulation of periodic processes
and real data sets are included. Hurd, H. L., Miamee, A. G. (2007)
<doi:10.1002/9780470182833> Box, G. E. P., Jenkins, G. M., Reinsel, G.
(1994) <doi:10.1111/jtsa.12194> Brockwell, P. J., Davis, R. A. (1991,
ISBN:978-1-4419-0319-8) Bretz, F., Hothorn, T., Westfall, P. (2010, ISBN:
9780429139543) Westfall, P. H., Young, S. S. (1993,
ISBN:978-0-471-55761-6) Bloomfield, P., Hurd, H. L.,Lund, R. (1994)
<doi:10.1111/j.1467-9892.1994.tb00181.x> Dehay, D., Hurd, H. L. (1994,
ISBN:0-7803-1023-3) Vecchia, A. (1985)
<doi:10.1080/00401706.1985.10488076> Vecchia, A. (1985)
<doi:10.1111/j.1752-1688.1985.tb00167.x> Jones, R., Brelsford, W. (1967)
<doi:10.1093/biomet/54.3-4.403> Makagon, A. (1999)
<https://www.math.uni.wroc.pl/~pms/files/19.2/Article/19.2.5.pdf> Sakai,
H. (1989) <doi:10.1111/j.1467-9892.1991.tb00069.x> Gladyshev, E. G. (1961)
<https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=dan&paperid=24851>
Ansley (1979) <doi:10.1093/biomet/66.1.59> Hurd, H. L., Gerr, N. L. (1991)
<doi:10.1111/j.1467-9892.1991.tb00088.x>.

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
