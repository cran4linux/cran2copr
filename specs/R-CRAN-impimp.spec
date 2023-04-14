%global __brp_check_rpaths %{nil}
%global packname  impimp
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Imprecise Imputation for Statistical Matching

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Imputing blockwise missing data by imprecise imputation, featuring a
domain-based, variable-wise, and case-wise strategy. Furthermore, the
estimation of lower and upper bounds for unconditional and conditional
probabilities based on the obtained imprecise data is implemented.
Additionally, two utility functions are supplied: one to check whether
variables in a data set contain set-valued observations; and another to
merge two already imprecisely imputed data. The method is described in a
technical report by Endres, Fink and Augustin (2018,
<doi:10.5282/ubm/epub.42423>).

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
