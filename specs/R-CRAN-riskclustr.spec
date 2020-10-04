%global packname  riskclustr
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          2%{?dist}%{?buildtag}
Summary:          Functions to Study Etiologic Heterogeneity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-stringr 
Requires:         R-Matrix 

%description
A collection of functions related to the study of etiologic heterogeneity
both across disease subtypes and across individual disease markers. The
included functions allow one to quantify the extent of etiologic
heterogeneity in the context of a case-control study, and provide p-values
to test for etiologic heterogeneity across individual risk factors. Begg
CB, Zabor EC, Bernstein JL, Bernstein L, Press MF, Seshan VE (2013) <doi:
10.1002/sim.5902>.

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
