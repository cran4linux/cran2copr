%global __brp_check_rpaths %{nil}
%global packname  zscorer
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Child Anthropometry z-Score Calculator

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-shiny 

%description
A tool for calculating z-scores and centiles for weight-for-age,
length/height-for-age, weight-for-length/height, BMI-for-age, head
circumference-for-age, age circumference-for-age, subscapular
skinfold-for-age, triceps skinfold-for-age based on the WHO Child Growth
Standards.

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
