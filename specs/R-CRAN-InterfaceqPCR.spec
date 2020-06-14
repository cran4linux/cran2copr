%global packname  InterfaceqPCR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          GUI to Analyse qPCR Results after PMA Treatment or not

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-plyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Graphical User Interface allowing to determine the concentration in the
sample in CFU per mL or in number of copies per mL provided to qPCR
results after with or without PMA treatment. This package is simply to use
because no knowledge in R commands is necessary. A graphic represents the
standard curve, and a table containing the result for each sample is
created.

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
%doc %{rlibdir}/%{packname}/a_laise_BZH2.gif
%doc %{rlibdir}/%{packname}/apropos.gif
%doc %{rlibdir}/%{packname}/calcul.gif
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/csv.gif
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Format_echantillons.gif
%doc %{rlibdir}/%{packname}/Format_gamme_etalon.gif
%doc %{rlibdir}/%{packname}/francais_flag.gif
%doc %{rlibdir}/%{packname}/GB_flag3.gif
%doc %{rlibdir}/%{packname}/help_icon.gif
%doc %{rlibdir}/%{packname}/jpg.gif
%doc %{rlibdir}/%{packname}/logoEAUDA.gif
%doc %{rlibdir}/%{packname}/Next.gif
%doc %{rlibdir}/%{packname}/pdf.gif
%doc %{rlibdir}/%{packname}/Plot.gif
%doc %{rlibdir}/%{packname}/PMAqPCR.gif
%doc %{rlibdir}/%{packname}/qPCR.gif
%doc %{rlibdir}/%{packname}/Rlogo.gif
%doc %{rlibdir}/%{packname}/start.gif
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/Thumbs.db
%doc %{rlibdir}/%{packname}/tiff.gif
%doc %{rlibdir}/%{packname}/Tubes.gif
%doc %{rlibdir}/%{packname}/xlsx_Fichiers_Echantillons.gif
%doc %{rlibdir}/%{packname}/xlsx_Fichiers_Standards.gif
%doc %{rlibdir}/%{packname}/xlsx.gif
%{rlibdir}/%{packname}/INDEX
