%global packname  curvecomp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Multiple Curve Comparisons Using Parametric Bootstrap

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp >= 0.4.8.0
Requires:         R-CRAN-multcomp >= 0.4.8.0

%description
Performs multiple comparison procedures on curve observations among
different treatment groups. The methods are applicable in a variety of
situations (such as independent groups with equal or unequal sample sizes,
or repeated measures) by using parametric bootstrap. References to these
procedures can be found at Konietschke, Gel, and Brunner (2014)
<doi:10.1090/conm/622/12431> and Westfall (2011)
<doi:10.1080/10543406.2011.607751>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
