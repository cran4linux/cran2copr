%global __brp_check_rpaths %{nil}
%global packname  colocalized
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Clusters of Colocalized Sequences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-purrr 
Requires:         R-utils 

%description
Also abbreviates to "CCSeq". Finds clusters of colocalized sequences in
.bed annotation files up to a specified cut-off distance. Two sequences
are colocalized if they are within the cut-off distance of each other, and
clusters are sets of sequences where each sequence is colocalized to at
least one other sequence in the cluster. For a set of .bed annotation
tables provided in a list along with a cut-off distance, the program will
output a file containing the locations of each cluster. Annotated .bed
files are from the 'pwmscan' application at
<https://ccg.epfl.ch/pwmtools/pwmscan.php>. Personal machines might crash
or take excessively long depending on the number of annotated sequences in
each file and whether chromsearch() or gensearch() is used.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
