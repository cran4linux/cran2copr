%global packname  BinMat
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Processes Binary Data Obtained from Fragment Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-base >= 3.4.0
BuildRequires:    R-CRAN-pvclust >= 2.0
BuildRequires:    R-CRAN-magrittr 
Requires:         R-MASS >= 7.3
Requires:         R-stats >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-base >= 3.4.0
Requires:         R-CRAN-pvclust >= 2.0
Requires:         R-CRAN-magrittr 

%description
A molecular genetics tool that processes binary data from fragment
analysis, such as inter-simple sequence repeats (ISSRs) and amplified
fragment length polymorphism (AFLP). It consolidates replicate sample
pairs, outputs summary statistics, and produces hierarchical clustering
trees and nMDS plots. This package was developed from the M.Sc. thesis
entitled "A genetic analysis of the species and intraspecific lineages of
Dactylopius Costa (Hemiptera:Dactylopiidae)" (van Steenderen, 2019, Rhodes
University, Department of Zoology and Entomology, Center for Biological
Control (CBC) <https://www.ru.ac.za/centreforbiologicalcontrol/>,
Grahamstown, South Africa), <doi:10.13140/RG.2.2.28470.86083>. The GUI
version of this package is available on the R Shiny online server at:
<https://clarkevansteenderen.shinyapps.io/BINMAT/> , or it is accessible
via GitHub by typing: shiny::runGitHub("BinMat", "CJMvS") into the console
in R. Please see the vignette supplied with the package for a worked
example, and detailed explanations of functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/INDEX
