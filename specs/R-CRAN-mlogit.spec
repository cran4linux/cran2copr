%global __brp_check_rpaths %{nil}
%global packname  mlogit
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multinomial Logit Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-statmod 
Requires:         R-MASS 
Requires:         R-CRAN-Rdpack 

%description
Maximum likelihood estimation of random utility discrete choice models.
The software is described in Croissant (2020) <doi:10.18637/jss.v095.i11>
and the underlying methods in Train (2009) <doi:10.1017/CBO9780511805271>.

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
