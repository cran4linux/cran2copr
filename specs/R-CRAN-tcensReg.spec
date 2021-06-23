%global __brp_check_rpaths %{nil}
%global packname  tcensReg
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          2%{?dist}%{?buildtag}
Summary:          MLE of a Truncated Normal Distribution with Censored Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-Rdpack 

%description
Maximum likelihood estimation (MLE) of parameters assuming an underlying
left truncated normal distribution with left censoring described in
Williams, J, Kim, H, and Crespi, C. (2020)
<doi:10.1186/s12874-020-01032-9>. Censoring is assumed to occur above the
truncation threshold meaning that only censored observations are observed.
Additional maximum likelihood estimation procedures are implemented to
solve left censored only and left truncated only problems.

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
