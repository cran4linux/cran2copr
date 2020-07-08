%global packname  pchc
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          2%{?dist}
Summary:          Bayesian Network Learning with the PCHC Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Bayesian network learning using the PCHC algorithm. PCHC stands for PC
Hill-Climbing. It is a new hybrid algorithm that used PC to construct the
skeleton of the BN and then utilizes the Hill-Climbing greedy search. The
relevant paper has been submitted and is currently in revision.

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