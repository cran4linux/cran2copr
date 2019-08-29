%global packname  kaphom
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Test the Homogeneity of Kappa Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Tests the homogeneity of intraclass kappa statistics obtained from
independent studies or a stratified study with binary results. It is
desired to compare the kappa statistics obtained in multi-center studies
or in a single stratified study to give a common or summary kappa using
all available information. If the homogeneity test of these kappa
statistics is not rejected, then it is possible to make inferences over a
single kappa statistic that summarizes all the studies. Muammer Albayrak,
Kemal Turhan, Yasemin Yavuz, Zeliha Aydin Kasap (2019)
<doi:10.1080/03610918.2018.1538457> Jun-mo Nam (2003)
<doi:10.1111/j.0006-341X.2003.00118.x> Jun-mo Nam (2005)
<doi:10.1002/sim.2321>Mousumi Banerjee, Michelle Capozzoli, Laura
McSweeney,Debajyoti Sinha (1999) <doi:10.2307/3315487> Allan Donner,
Michael Eliasziw, Neil Klar (1996) <doi:10.2307/2533154>.

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
