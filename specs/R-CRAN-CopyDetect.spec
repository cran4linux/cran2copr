%global packname  CopyDetect
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Computing Response Similarity Indices for Multiple-Choice Tests

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
Requires:         R-CRAN-mirt 

%description
Contains several IRT and non-IRT based response similarity indices
proposed in the literature for multiple-choice examinations such as the
Omega index, Wollack (1997) <doi:10.1177/01466216970214002>; Generalized
Binomial Test, van der Linden & Sotaridona (2006)
<doi:10.3102/10769986031003283>; K index, K1 and K2 indices, Sotaridona &
Meijer (2002) <doi:10.1111/j.1745-3984.2002.tb01138.x>; and S1 and S2
indices, Sotaridona & Meijer (2003)
<doi:10.1111/j.1745-3984.2003.tb01096.x>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
