%global packname  semnova
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Latent Repeated Measures ANOVA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-lavaan 
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-methods 

%description
Latent repeated measures ANOVA (L-RM-ANOVA) is a structural equation
modeling based alternative to traditional repeated measures ANOVA.
L-RM-ANOVA extends the latent growth components approach by Mayer et al.
(2012) <doi:10.1080/10705511.2012.713242> and introduces latent variables
to repeated measures analysis.

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
