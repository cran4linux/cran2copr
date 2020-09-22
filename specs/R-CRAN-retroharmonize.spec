%global packname  retroharmonize
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Ex Post Survey Data Harmonization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-here 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-labelled 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-here 

%description
Assist in reproducible retrospective (ex-post) harmonization of data,
particularly individual level survey data, by providing tools for
organizing metadata, standardizing the coding of variables, and variable
names and value labels, including missing values, and documenting the data
transformations, with the help of comprehensive s3 classes.

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
