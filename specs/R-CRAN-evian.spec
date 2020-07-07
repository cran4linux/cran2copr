%global packname  evian
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}
Summary:          Evidential Analysis of Genetic Association Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ProfileLikelihood 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-ProfileLikelihood 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Evidential regression analysis for dichotomous and quantitative outcome
data. The following references described the methods in this package:
Strug, L. J., Hodge, S. E., Chiang, T., Pal, D. K., Corey, P. N., & Rohde,
C. (2010) <doi:10.1038/ejhg.2010.47>. Strug, L. J., & Hodge, S. E. (2006)
<doi:10.1159/000094709>. Royall, R. (1997) <ISBN:0-412-04411-0>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
