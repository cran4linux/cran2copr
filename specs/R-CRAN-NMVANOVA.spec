%global __brp_check_rpaths %{nil}
%global packname  NMVANOVA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Novice Model Variation ANOVA

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Due to 'Rstudio's' status as open source software, we believe it will be
utilized frequently for future data analysis by users whom lack formal
training or experience with 'R'. The 'NMVANOVA' (Novice Model Variation
ANOVA) a streamlined variation of experimental design functions that
allows novice 'Rstudio' users to perform different model variations
one-way analysis of variance without downloading multiple libraries or
packages. Users can easily manipulate the data block, and needed inputs so
that users only have to plugin the four designed variables/values.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
