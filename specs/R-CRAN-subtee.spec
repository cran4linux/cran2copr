%global packname  subtee
%global packver   0.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Subgroup Treatment Effect Estimation in Clinical Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-survival 
Requires:         R-CRAN-matrixStats 

%description
Naive and adjusted treatment effect estimation for subgroups. Model
averaging (Bornkamp et.al, 2016 <doi:10.1002/pst.1796>) and bagging
(Rosenkranz, 2016 <doi:10.1002/bimj.201500147>) are proposed to address
the problem of selection bias in treatment effect estimates for subgroups.
The package can be used for all commonly encountered type of outcomes in
clinical trials (continuous, binary, survival, count). Additional
functions are provided to build the subgroup variables to be used and to
plot the results using forest plots.

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
