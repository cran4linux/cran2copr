%global packname  TraMineR
%global packver   2.2-0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Trajectory Miner: a Toolbox for Exploring and RenderingSequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-boot 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-utils 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-boot 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 
Requires:         R-cluster 
Requires:         R-CRAN-colorspace 

%description
Toolbox for the manipulation, description and rendering of sequences, and
more generally the mining of sequence data in the field of social
sciences. Although the toolbox is primarily intended for analyzing state
or event sequences that describe life courses such as family formation
histories or professional careers, its features also apply to many other
kinds of categorical sequence data. It accepts many different sequence
representations as input and provides tools for converting sequences from
one format to another. It offers several functions for describing and
rendering sequences, for computing distances between sequences with
different metrics (among which optimal matching), original
dissimilarity-based analysis tools, and simple functions for extracting
the most frequent subsequences and identifying the most discriminating
ones among them. A user's guide can be found on the TraMineR web page.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
