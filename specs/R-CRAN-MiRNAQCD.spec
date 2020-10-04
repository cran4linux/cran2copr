%global packname  MiRNAQCD
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Micro-RNA Quality Control and Diagnosis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 

%description
A complete and dedicated analytical toolbox for quality control and
diagnosis based on subject-related measurements of micro-RNA (miRNA)
expressions. The package consists of a set of functions that allow to
train, optimize and use a Bayesian classifier that relies on multiplets of
measured miRNA expressions. The package also implements the quality
control tools required to preprocess input datasets. In addition, the
package provides a function to carry out a statistical analysis of miRNA
expressions, which can give insights to improve the classifier's
performance. The method implemented in the package was first introduced in
L. Ricci, V. Del Vescovo, C. Cantaloni, M. Grasso, M. Barbareschi and M.
A. Denti, "Statistical analysis of a Bayesian classifier based on the
expression of miRNAs", BMC Bioinformatics 16:287, 2015
<doi:10.1186/s12859-015-0715-9>. The package is thoroughly described in M.
Castelluzzo, A. Perinelli, S. Detassis, M. A. Denti and L. Ricci,
"MiRNA-QC-and-Diagnosis: An R package for diagnosis based on MiRNA
expression", SoftwareX 12:100569, 2020 <doi:10.1016/j.softx.2020.100569>.
Please cite both these works if you use the package for your analysis.
DISCLAIMER: The software in this package is for general research purposes
only and is thus provided WITHOUT ANY WARRANTY. It is NOT intended to form
the basis of clinical decisions. Please refer to the GNU General Public
License 3.0 (GPLv3) for further information.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
