%global packname  documair
%global packver   0.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Automatic Documentation for R packages

License:          GPL (>= 2.15)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Production of R packages from tagged comments introduced within the code
and a minimum of additional documentation files.

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
%doc %{rlibdir}/%{packname}/2014_09_12-10_28_29.make.r
%doc %{rlibdir}/%{packname}/basic.code.r
%doc %{rlibdir}/%{packname}/basic.test1.r
%doc %{rlibdir}/%{packname}/builder.code.r
%{rlibdir}/%{packname}/builder.data1.txt
%doc %{rlibdir}/%{packname}/builder.test1.r
%doc %{rlibdir}/%{packname}/builder.test1.txt
%doc %{rlibdir}/%{packname}/builder.test2.r
%doc %{rlibdir}/%{packname}/builder.test2.txt
%doc %{rlibdir}/%{packname}/builder.tests.r
%doc %{rlibdir}/%{packname}/display.code.r
%{rlibdir}/%{packname}/documair.DESCRIPTION
%doc %{rlibdir}/%{packname}/documair.package.Rd
%doc %{rlibdir}/%{packname}/documair.which.txt
%{rlibdir}/%{packname}/documair1.DESCRIPTION
%doc %{rlibdir}/%{packname}/documair1.package.Rd
%{rlibdir}/%{packname}/documair2.DESCRIPTION
%doc %{rlibdir}/%{packname}/documair2.package.Rd
%doc %{rlibdir}/%{packname}/documair2.which.txt
%{rlibdir}/%{packname}/documair3.DESCRIPTION
%doc %{rlibdir}/%{packname}/documair3.package.Rd
%doc %{rlibdir}/%{packname}/documair3.which.txt
%doc %{rlibdir}/%{packname}/exterieur.coding.r
%doc %{rlibdir}/%{packname}/fonction
%doc %{rlibdir}/%{packname}/make.r
%doc %{rlibdir}/%{packname}/objects.code.r
%doc %{rlibdir}/%{packname}/pert.alias.r
%doc %{rlibdir}/%{packname}/readme.txt
%doc %{rlibdir}/%{packname}/rrbsa.code.r
%{rlibdir}/%{packname}/rrbsa.DESCRIPTION
%doc %{rlibdir}/%{packname}/rrbsa.essairrbsa.r
%doc %{rlibdir}/%{packname}/rrbsa.package.Rd
%doc %{rlibdir}/%{packname}/rrbsa.r
%doc %{rlibdir}/%{packname}/rrbsa.which.txt
%doc %{rlibdir}/%{packname}/sumc.c
%doc %{rlibdir}/%{packname}/sumf.f
%doc %{rlibdir}/%{packname}/text.code.r
%doc %{rlibdir}/%{packname}/text.test1.r
%doc %{rlibdir}/%{packname}/user.code.r
%doc %{rlibdir}/%{packname}/user.test1.r
%doc %{rlibdir}/%{packname}/user.tests.r
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
