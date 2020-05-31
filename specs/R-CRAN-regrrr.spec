%global packname  regrrr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Toolkit for Compiling, (Post-Hoc) Testing, and PlottingRegression Results

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-usdm 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lspline 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-usdm 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lspline 

%description
Compiling regression results into a publishable format, conducting
post-hoc hypothesis testing, and plotting moderating effects (the effect
of X on Y becomes stronger/weaker as Z increases).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
