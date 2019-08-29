%global packname  gluvarpro
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Glucose Variability Measures from Continuous Glucose MonitoringData

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 

%description
Calculate different glucose variability measures, including average
measures of glycemia, measures of glycemic variability and measures of
glycemic risk, from continuous glucose monitoring data obtained from
diabetic patients. Boris P. Kovatchev, Erik Otto, Daniel Cox, Linda
Gonder-Frederick, and William Clarke (2006) <doi:10.2337/dc06-1085>.
Jean-Pierre Le Floch, Philippe Escuyer, Eric Baudin, Dominique Baudon, and
Leon Perlemuter (1990) <doi:10.2337/diacare.13.2.172>. C.M. McDonnell,
S.M. Donath, S.I. Vidmar, G.A. Werther, and F.J. Cameron (2005)
<doi:10.1089/dia.2005.7.253>. Everitt, Brian (1998)
<doi:10.1111/j.1751-5823.2011.00149_2.x>. Becker, R. A., Chambers, J. M.
and Wilks, A. R. (1988) <doi:10.2307/2234167>. Dougherty, R. L., Edelman,
A. and Hyman, J. M. (1989) <doi:10.1090/S0025-5718-1989-0962209-1>. Tukey,
J. W. (1977) <doi:10.1016/0377-2217(86)90209-2>. F. John Service (2013)
<doi:10.2337/db12-1396>. Edmond A. Ryan, Tami Shandro, Kristy Green, Breay
W. Paty, Peter A. Senior, David Bigam, A.M. James Shapiro, and
Marie-Christine Vantyghem (2004) <doi:10.2337/diabetes.53.4.955>. Seniz
Sevimer Tuncan, Mehmet Uzunlulu, Ozge telci caklili, Hasan Huseyin Mutlu,
and Aytekin Oguz (2016) <doi:10.5152/cjms.2016.109>. Sarah E. Siegelaar,
Frits Holleman, Joost B. L. Hoekstra, and J. Hans DeVries (2010)
<doi:10.1210/er.2009-0021>. Gabor Marics, Zsofia Lendvai, Csaba Lodi,
Levente Koncz, David Zakarias, Gyorgy Schuster, Borbala Mikos, Csaba
Hermann, Attila J. Szabo, and Peter Toth-Heyn (2015)
<doi:10.1186/s12938-015-0035-3>.

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
