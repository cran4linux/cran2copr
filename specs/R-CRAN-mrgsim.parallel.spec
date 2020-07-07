%global packname  mrgsim.parallel
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Simulate with 'mrgsolve' in Parallel

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mrgsolve 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-mrgsolve 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future.apply 

%description
Simulation from an 'mrgsolve'
<https://cran.r-project.org/package=mrgsolve> model using a parallel
backend. Input data sets are split (chunked) and simulated in parallel
using mclapply() or future_lapply()
<https://cran.r-project.org/package=future.apply>.

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
