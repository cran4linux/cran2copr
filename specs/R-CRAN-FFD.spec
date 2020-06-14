%global packname  FFD
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          2%{?dist}
Summary:          Freedom from Disease

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         bwidget
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-R2HTML 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-R2HTML 

%description
Functions, S4 classes/methods and a graphical user interface (GUI) to
design surveys to substantiate freedom from disease using a modified
hypergeometric function (see Cameron and Baldock, 1997). Herd
sensitivities are computed according to sampling strategies "individual
sampling" or "limited sampling" (see M. Ziller, T. Selhorst, J. Teuffert,
M. Kramer and H. Schlueter, 2002). Methods to compute the a-posteriori
alpha-error are implemented. Risk-based targeted sampling is supported.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/GUI_Logo.ppm
%doc %{rlibdir}/%{packname}/GUI_Logo2.ppm
%doc %{rlibdir}/%{packname}/GUI_Logo3.ppm
%doc %{rlibdir}/%{packname}/GUI_Logo4.ppm
%doc %{rlibdir}/%{packname}/sheepData.csv
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
