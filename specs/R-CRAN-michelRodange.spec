%global __brp_check_rpaths %{nil}
%global packname  michelRodange
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          The Works (in Luxembourguish) of Michel Rodange

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-magrittr 

%description
Michel Rodange was a Luxembourguish writer and poet who lived in the 19th
century. His most notable work is Rodange (1872, ISBN:1166177424),
("Renert oder de Fuuß am Frack an a Ma'nsgrëßt"), but he also wrote many
more works, including Rodange, Tockert (1928)
<https://www.autorenlexikon.lu/page/document/361/3614/1/FRE/index.html>
("D'Léierchen - Dem Léiweckerche säi Lidd") and Rodange, Welter (1929)
<https://www.autorenlexikon.lu/page/document/361/3615/1/FRE/index.html>
("Dem Grow Sigfrid seng Goldkuommer"). This package contains three
datasets, each made from the plain text versions of his works available on
<https://data.public.lu/fr/datasets/the-works-in-luxembourguish-of-michel-rodange/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
